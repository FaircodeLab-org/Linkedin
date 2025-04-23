import frappe
from frappe.model.document import Document
import requests
import os
from urllib.parse import unquote

url = "https://api.linkedin.com/v2/ugcPosts"
    
token = frappe.db.get_value("LinkedIn Configuration", None, "access_token", as_dict=False)
company_id = frappe.db.get_value("LinkedIn Configuration", None, "company_id")

def get_new_access_token():
    refresh_url = "https://www.linkedin.com/oauth/v2/accessToken"
    refresh_token = frappe.db.get_value("LinkedIn Configuration", None, "refresh_token", as_dict=False)
    client_id = frappe.db.get_value("LinkedIn Configuration", None, "client_id")
    client_secret = frappe.db.get_value("LinkedIn Configuration", None, "client_secret")

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(refresh_url, data=payload, headers=headers)
    
    if response.status_code == 200:
        new_token_data = response.json()
        new_access_token = new_token_data.get("access_token")
        
        frappe.db.set_value("LinkedIn Configuration", None, "access_token", new_access_token)
        frappe.db.commit()
        print('updated the access token')

        return new_access_token
    else:
        frappe.log_error(response.text, "LinkedIn Token Refresh Failed")
        return None



def text_post(doc, method):

    visibility = doc.visibility if doc.visibility else "PUBLIC"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "author": f"urn:li:organization:{company_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": doc.text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": visibility 
        }
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        response_data = response.json()
        doc.post_status = "Published"
        doc.post_id = response_data.get("id")
    elif response.status_code == 401:
        new_token = get_new_access_token()
        if new_token:
            headers["Authorization"] = f"Bearer {new_token}"
            retry_response = requests.post(url, json=payload, headers=headers)
            if retry_response.status_code == 201:
                response_data = retry_response.json()
                doc.post_status = "Published"
                doc.post_id = response_data.get("id")
            else:
                doc.post_status = "Failed"
                doc.api_response = retry_response.text
        else:
            doc.post_status = "Failed"
            doc.api_response = "Token refresh failed."
    else:
        doc.post_status = "Failed"
        doc.api_response = response.text


def post_article(doc, method):
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
    "author": f"urn:li:organization:{company_id}",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": doc.post
            },
            "shareMediaCategory": "ARTICLE",
            "media": [
                {
                    "status": "READY",
                    "originalUrl": doc.url,
                    "title": {
                        "text": doc.title
                    },
                    "description": {
                        "text": doc.description
                    }
                }
            ]
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        response_data = response.json()
        doc.post_status = "Published"
        doc.post_id = response_data.get("id")
    elif response.status_code == 401:
        new_token = get_new_access_token()
        if new_token:
            headers["Authorization"] = f"Bearer {new_token}"
            retry_response = requests.post(url, json=payload, headers=headers)
            if retry_response.status_code == 201:
                response_data = retry_response.json()
                doc.post_status = "Published"
                doc.post_id = response_data.get("id")
            else:
                doc.post_status = "Failed"
                doc.api_response = retry_response.text
        else:
            doc.post_status = "Failed"
            doc.api_response = "Token refresh failed."
    else:
        doc.post_status = "Failed"
        doc.api_response = response.text


def get_file_content(file_path):
    file_path = unquote(file_path)
    
    if file_path.startswith("/private/files") or file_path.startswith("/files"):
        local_path = frappe.utils.get_site_path("public", file_path.lstrip("/"))
        
        if os.path.exists(local_path):
            return open(local_path, "rb")
        else:
            raise FileNotFoundError(f"File not found at: {local_path}")
    else:
        response = requests.get(file_path, stream=True)
        if response.status_code == 200:
            return response.raw
        else:
            raise Exception(f"Failed to download file from: {file_path}")

def post_image(doc, method):
    register_url = "https://api.linkedin.com/v2/assets?action=registerUpload"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    register_payload = {
        "registerUploadRequest": {
            "owner": f"urn:li:organization:{company_id}",
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
            "serviceRelationships": [
                {
                    "identifier": "urn:li:userGeneratedContent",
                    "relationshipType": "OWNER"
                }
            ]
        }
    }

    register_response = requests.post(register_url, json=register_payload, headers=headers)

    if register_response.status_code == 401:
        print("Access token expired, refreshing token...")
        new_token = get_new_access_token()
        if new_token:
            headers["Authorization"] = f"Bearer {new_token}"
            register_response = requests.post(register_url, json=register_payload, headers=headers)
    
    if register_response.status_code != 200:
        print(f"Failed to register upload: {register_response.text}")
        doc.post_status = "Failed"
        doc.api_response = register_response.text
        return

    register_data = register_response.json()
    upload_url = register_data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]
    asset = register_data["value"]["asset"]

    image_file_path = frappe.get_site_path("public", "files", doc.image)
    try:
        with get_file_content(doc.image) as image_file:
            upload_response = requests.put(upload_url, headers={"Authorization": f"Bearer {token}"}, data=image_file)

        if upload_response.status_code != 201:
            print(f"Failed to upload image: {upload_response.text}")
            doc.post_status = "Failed"
            doc.api_response = upload_response.text
            return

    except Exception as e:
        print(f"Error uploading the image: {e}")
        doc.post_status = "Failed"
        doc.api_response = str(e)
        return

    post_payload = {
        "author": f"urn:li:organization:{company_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": doc.text or "Check out this image!" 
                },
                "shareMediaCategory": "IMAGE",
                "media": [
                    {
                        "status": "READY",
                        "description": {"text": doc.description or "Image description"}, 
                        "media": asset 
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    post_response = requests.post(url, json=post_payload, headers=headers)

    if post_response.status_code == 201:
        response_data = post_response.json()
        doc.post_status = "Published"
        doc.post_id = response_data.get("id")
    else:
        print(f"Failed to create LinkedIn post: {post_response.text}")
        doc.post_status = "Failed"
        doc.api_response = post_response.text

    
def post_video(doc, method):

    register_url = "https://api.linkedin.com/v2/assets?action=registerUpload"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    register_payload = {
        "registerUploadRequest": {
            "owner": f"urn:li:organization:{company_id}",
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-video"],
            "serviceRelationships": [
                {
                    "identifier": "urn:li:userGeneratedContent",
                    "relationshipType": "OWNER"
                }
            ]
        }
    }

    register_response = requests.post(register_url, json=register_payload, headers=headers)
    if register_response.status_code == 401:
        print("Access token expired, refreshing token...")
        new_token = get_new_access_token()
        if new_token:
            headers["Authorization"] = f"Bearer {new_token}"
            register_response = requests.post(register_url, json=register_payload, headers=headers)
    
    if register_response.status_code != 200:
        print(f"Failed to register upload: {register_response.text}")
        doc.post_status = "Failed"
        doc.api_response = register_response.text
        return

    register_data = register_response.json()
    upload_url = register_data["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]
    asset = register_data["value"]["asset"]

    video_file_path = frappe.get_site_path("public", "files", doc.video)  
    try:
        with get_file_content(doc.video) as video_file:
            upload_response = requests.put(upload_url, headers={"Authorization": f"Bearer {token}"}, data=video_file)

        if upload_response.status_code != 201:
            print(f"Failed to upload video: {upload_response.text}")
            doc.post_status = "Failed"
            doc.api_response = upload_response.text
            return

    except Exception as e:
        print(f"Error uploading the video: {e}")
        doc.post_status = "Failed"
        doc.api_response = str(e)
        return

    post_payload = {
        "author": f"urn:li:organization:{company_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": doc.text or "Check out this video!"
                },
                "shareMediaCategory": "VIDEO",
                "media": [
                    {
                        "status": "READY",
                        "description": {"text": doc.description or "Video description"}, 
                        "media": asset 
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    post_response = requests.post(url, json=post_payload, headers=headers)

    if post_response.status_code == 201:
        response_data = post_response.json()
        doc.post_status = "Published"
        doc.post_id = response_data.get("id")
    else:
        print(f"Failed to create LinkedIn post: {post_response.text}")
        doc.post_status = "Failed"
        doc.api_response = post_response.text
