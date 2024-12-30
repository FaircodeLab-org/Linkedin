# LinkedIn Integration App for Frappe

This app integrates Frappe with LinkedIn, enabling seamless posting of images, videos, articles, and text updates to LinkedIn directly from your Frappe environment.

## Features
- Post Text, Articles, Images, and Videos directly from Frappe without uploading files to the file manager.
- Automatic refresh of expired LinkedIn access tokens for uninterrupted API functionality.
- Custom Doctypes for managing LinkedIn-related content and settings.
- Integration with LinkedIn API endpoints to register uploads, post content, and manage assets.

## Installation
1. Clone the repository: `bench get-app https://github.com/FaircodeLab-org/Linkedin/tree/main`
2. Install the app on your site: `bench --site [your-site-name] install-app linkedin`
3. Set up the necessary LinkedIn API credentials in the **LinkedIn Settings** doctype.

## Configuration
### LinkedIn API Credentials
To use the app, configure the following:
- Client ID
- Client Secret
- Access Token
- Refresh Token
- Company ID (for organization posts)

### Setting Up LinkedIn Settings
1. Navigate to **LinkedIn Settings** in your site.
2. Enter the required API credentials.
3. Save the settings.

## Usage
### Posting Content
1. Choose the doctype based on the type of content:
   - Text Post: For text updates.
   - Article Post: For articles.
   - Image Post: For image updates.
   - Video Post: For video updates.
2. Fill out the fields in the selected doctype with the required details.
3. **Important:** When posting images or videos, ensure that they are set to **public**. If the content is not made public, it will not be published on LinkedIn.
4. Save and submit the record to post the content on LinkedIn.

### Token Management
The app automatically refreshes expired LinkedIn access tokens.

## API Endpoints
- Register Upload: `https://api.linkedin.com/v2/assets?action=registerUpload`
- Upload Image/Video: Uses upload URL from the register response.
- Create Post: `https://api.linkedin.com/v2/ugcPosts`
- Refresh Token: `https://www.linkedin.com/oauth/v2/accessToken`

## Development
### Prerequisites
- Python 3.x
- Frappe Framework

### Local Development Setup
1. Clone the repository into your Frappe apps directory.
2. Install the app on a test site using the installation commands.
3. Configure LinkedIn credentials in the test site.

### Updating Dependencies
Generate or update the `requirements.txt` file: `pip freeze > requirements.txt`

## Troubleshooting
### Common Issues
- **401 Unauthorized Error:**  
  - Cause: Expired access token.  
  - Solution: Ensure `refresh_token`, `client_id`, and `client_secret` are configured correctly.
- **Image/Video Upload Fails:**  
  - Cause: Invalid file URL or incorrect upload mechanism.  
  - Solution: Verify the file URL and retry the upload.

### Logs
Check error logs in Frappe: `bench --site [your-site-name] console`

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
We welcome contributions! Submit issues and pull requests to help improve this app.

## Acknowledgments
- [LinkedIn API Documentation](https://learn.microsoft.com/en-us/linkedin/)
- [Frappe Framework](https://frappeframework.com/)
