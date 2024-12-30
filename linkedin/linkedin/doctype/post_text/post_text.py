# Copyright (c) 2024, Mirshad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests


class PostText(Document):
	pass



# def post_to_linkedin(doc, method):
#     print("Posting to LinkedIn...")
#     # API Endpoint
#     url = "https://api.linkedin.com/v2/ugcPosts"
    
#     # Authorization Token
#     token = frappe.db.get_value("LinkedIn Settings", None, "access_token")
#     company_id = frappe.db.get_value("LinkedIn Settings", None, "company_id")
#     print(token)
#     print(company_id)
    
#     # Headers
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json"
#     }
    
#     # Post Data
#     payload = {
#         "author": f"urn:li:organization:{company_id}",
#         "lifecycleState": "PUBLISHED",
#         "specificContent": {
#             "com.linkedin.ugc.ShareContent": {
#                 "shareCommentary": {
#                     "text": doc.text
#                 },
#                 "shareMediaCategory": "NONE"
#             }
#         },
#         "visibility": {
#             "com.linkedin.ugc.MemberNetworkVisibility": {doc.visibility}
#         }
#     }
    
#     # Make API Call
#     response = requests.post(url, json=payload, headers=headers)
    
#     # Handle Response
#     if response.status_code == 201:
#         response_data = response.json()
#         doc.post_status = "Published"
#         doc.post_id = response_data.get("id")
#     else:
#         doc.post_status = "Failed"
#         doc.api_response = response.text
