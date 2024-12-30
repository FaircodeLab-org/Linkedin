app_name = "linkedin"
app_title = "Linkedin"
app_publisher = "Mirshad"
app_description = "To integrate linkedin with ERPNext"
app_email = "abdullamirshadcl@gmail.com"
app_license = "mit"

fixtures = [
    {"doctype": "Workspace", "filters": [["module", "=", "linkedin"]]}
]
# doctype_js = {
#     "Linkedin Settings": "linkedin/doctype/linkedin_settings/linkedin_settings.js"
# }

# doc_events = {
#     "Linkedin Settings": {
#         "before_save": "linkedin.linkedin.doctype.linkedin_settings.linkedin_settings.before_save_linkedin_settings"
#     }
# }
doc_events = {
    "Post Text": {
        "before_submit": "linkedin.linkedin_post.text_post"
    }, 
    "Post Article": {
        "before_submit": "linkedin.linkedin_post.post_article"
    }, 
    "Post Image": {
        "before_submit": "linkedin.linkedin_post.post_image"
    }, 
    "Post Video": {
        "before_submit": "linkedin.linkedin_post.post_video"
    }, 
}


# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "linkedin",
# 		"logo": "/assets/linkedin/logo.png",
# 		"title": "Linkedin",
# 		"route": "/linkedin",
# 		"has_permission": "linkedin.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/linkedin/css/linkedin.css"
# app_include_js = "/assets/linkedin/js/linkedin.js"

# include js, css files in header of web template
# web_include_css = "/assets/linkedin/css/linkedin.css"
# web_include_js = "/assets/linkedin/js/linkedin.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "linkedin/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "linkedin/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "linkedin.utils.jinja_methods",
# 	"filters": "linkedin.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "linkedin.install.before_install"
# after_install = "linkedin.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "linkedin.uninstall.before_uninstall"
# after_uninstall = "linkedin.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "linkedin.utils.before_app_install"
# after_app_install = "linkedin.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "linkedin.utils.before_app_uninstall"
# after_app_uninstall = "linkedin.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "linkedin.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"linkedin.tasks.all"
# 	],
# 	"daily": [
# 		"linkedin.tasks.daily"
# 	],
# 	"hourly": [
# 		"linkedin.tasks.hourly"
# 	],
# 	"weekly": [
# 		"linkedin.tasks.weekly"
# 	],
# 	"monthly": [
# 		"linkedin.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "linkedin.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "linkedin.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "linkedin.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["linkedin.utils.before_request"]
# after_request = ["linkedin.utils.after_request"]

# Job Events
# ----------
# before_job = ["linkedin.utils.before_job"]
# after_job = ["linkedin.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"linkedin.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

