// frappe.ui.form.on('Linkedin Settings', {
//     before_save: function (frm) {
//         if (frm.doc.access_token) {
//             frappe.call({
//                 method: "linkedin.linkedin.doctype.linkedin_settings.linkedin_settings.fetch_linkedin_urn",
//                 args: { access_token: frm.doc.access_token },
//                 callback: function (response) {
//                     console.log(response); // Log the API response for debugging
//                     if (response.message && response.message.user_id) {
//                         frm.set_value('user_id', response.message.user_id);
//                         frappe.msgprint('User ID retrieved and saved successfully.');
//                     } else {
//                         frappe.msgprint('Failed to retrieve User ID. Please check your Access Token.');
//                     }
//                 },
//                 error: function (error) {
//                     frappe.msgprint('Failed to retrieve User ID. Please check the console for details.');
//                     console.error(error);
//                 },
//             });
//         } else {
//             frappe.msgprint('Please provide a valid Access Token before saving.');
//         }
//     },
// });
