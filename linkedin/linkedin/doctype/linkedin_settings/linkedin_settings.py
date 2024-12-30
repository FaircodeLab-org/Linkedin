# import requests
# import frappe
from frappe.model.document import Document

class Linkedinsettings(Document):
    """
    Custom LinkedIn Settings Document Class
    """
    pass

# @frappe.whitelist()
# def fetch_linkedin_urn(access_token):
#     """
#     Fetch the URN from LinkedIn API using the provided access token.
#     """
#     api_url = "https://api.linkedin.com/v2/userinfo"  # Replace with the correct LinkedIn API endpoint
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json",
#     }

#     try:
#         response = requests.get(api_url, headers=headers)
#         response.raise_for_status()
#         data = response.json()
#         frappe.log_error(data, "LinkedIn API Response")  # Log response for debugging
#         user_id = data.get("sub")  # Adjust based on LinkedIn API response structure
#         return {"user_id": user_id}
#     except requests.exceptions.RequestException as e:
#         frappe.log_error(str(e), "LinkedIn API Error")  # Log error for debugging
#         frappe.throw(_("Failed to fetch LinkedIn URN: {0}").format(str(e)))

# def before_save_linkedin_settings(doc, method):
#     """
#     Before saving the LinkedIn Settings document, fetch and set the URN.
#     """
#     if doc.access_token:
#         urn_response = fetch_linkedin_urn(doc.access_token)
#         frappe.log_error(urn_response, "URN Response")  # Log the URN response for debugging
#         if urn_response.get("user_id"):
#             doc.user_id = urn_response.get("user_id")
#         else:
#             frappe.throw(_("Failed to fetch URN from LinkedIn."))
