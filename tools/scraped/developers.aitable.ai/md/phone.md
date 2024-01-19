Search Getting StartedExamplesData matcherFind the phone number in a column On this page

## Find The Phone Number In A Column

INFO
Support finding and displaying phone numbers in a specified format in a column of data, such as +1-650-555-1234

## Demo

The following is example data, not real phone number

## Source Code

 datasheet =  space.getActiveDatasheetAsync(); phoneField =  input.fieldAsync("Please select the text column where the phone number is listed:", datasheet const phoneFieldId = phoneField.id; /* This regrex matches phone numbers that start with a + sign, * followed by three groups of digits separated by either a hyphen - or whitespace. * The groups can have any number of digits, and the final group must end with at least one digit. * If you need to match phone numbers in a different format, you can modify the regular expression accordingly. */ const regexReg = /^\+(?:[0-9]+[\-\s]*){3}[0-9]+$/; const records = *await* datasheet.getRecordsAsync(); const finalData = ['Matched Phone Number'];
for (let record of records) { let cellValue = record.getCellValue(phoneFieldId); if (cellValue == null) *continue*; *const* validation = cellValue.match(regexReg); if (validation != *null*) { finalData.push(record.getCellValueString(phoneFieldId)); } }
if (finalData.length){
  output.table(finalData); } *else* { output.text("No matching data") }
Previous « Find the id card number in a column Developer Center Development guide API Reference Social Twitter More Homepage Help Center GitHub Next Link records with duplicate values »