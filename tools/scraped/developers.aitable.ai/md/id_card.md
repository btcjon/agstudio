Search Getting StartedExamplesData matcherFind the id card number in a column On this page

## Find The Id Card Number In A Column

INFO
Support to find the id card number of "xxxxx-xxxxx-x" where x are all numbers in a column of data and display it

## Demo

The following is example data, not real ID Card number Source Code datasheet =  space.getActiveDatasheetAsync(); idCardField =  input.fieldAsync("Please select the text column where the id card number is listed:", datasheet const idCardFieldId = idCardField.id; // you can customize this regex to suit your needs const regexReg = /^\d{5}-\d{5}-\d$/; const records = *await* datasheet.getRecordsAsync(); const finalData = ['Matched ID Card Number']; for (let record of records) { let cellValue = record.getCellValue(idCardFieldId);
  if (cellValue == null) *continue*; *const* validation = cellValue.match(regexReg); if (validation != *null*) { finalData.push(record.getCellValueString(idCardFieldId)); } } if (finalData.length){ output.table(finalData); } *else* {
  output.text("No matching data")
}
Previous « Verify whether the email is legal Developer Center Development guide API Reference Social Twitter More Homepage Help Center GitHub Next Find the phone number in a column »