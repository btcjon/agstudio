Search Getting StartedExamplesExtract URL from attachment On this page

## Extract Url From Attachment

INFO
Support converting attachments into links that can be accessed directly Demo Source code datasheet =  space.getActiveDatasheetAsync(); attachmentField =  input.fieldAsync(
  "Please select the attachment field:",
  datasheet ); const urlField = *await* input.fieldAsync( "Please select the URL field:", datasheet ); const isCover = *await* input.textAsync(
  "Whether to overwrite existing URLs (yes/no):" ); // If the value entered in "Whether to overwrite the existing URL" is not "Yes" or "No", a relevant prompt will be given if (isCover != "yes" && isCover != "no") { output.text("Please enter the correct value!!!"); } *else* { *const* urlFieldId = urlField.id; *const* attachmentFieldId = attachmentField.id; *const* records = *await* datasheet.getRecordsAsync(); for (let record of records) {
    *const* recordId = record.id;
    *const* attachmentCellValue = record.getCellValue(attachmentFieldId); *const* urlCellValue = record.getCellValueString(urlFieldId); //The empty data does not belong to the content to be converted into URL, so it is skipped if (attachmentCellValue == null) *continue*; if (isCover == "no" && urlCellValue != null) *continue*; // Get the url value of the attachment *const* url = attachmentCellValue[0].url; datasheet.updateRecordAsync(recordId, { [urlFieldId]: url }); } output.text("Attachment converted to URL!!!"); }
Previous « Link records with duplicate values Developer Center Development guide API Reference Social Twitter More Homepage Help Center GitHub Next Generate latitude and longitude from IP address »