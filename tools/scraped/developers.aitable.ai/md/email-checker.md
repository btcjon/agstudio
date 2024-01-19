Search Getting StartedExamplesData matcherVerify whether the email is legal On this page

## Verify Whether The Email Is Legal Info

Supports checking whether the email meets the specified requirements in the text type column, and if it does, it will be marked as √ in the corresponding checkbox column

## Demo

The following is example data, not real email

## Source Code

 datasheet =  space.getActiveDatasheetAsync(); mailField =  input.fieldAsync("Please select the text column where the email address is located:", datasheet const mailFieldId = mailField.id; const checkField = *await* input.fieldAsync("Please select the check field, which needs to be a check type:", datasheet const checkFieldId = checkField.id; const records = *await* datasheet.getRecordsAsync(); const mailRule = *await* input.textAsync('Please enter the email suffix, such as @aitable.ai:'); const mailReg = new RegExp(mailRule); const finalData = [];
for (let record of records) { *const* recordId = record.id; let cellValue = record.getCellValue(mailFieldId); if (cellValue == null) *continue*; *const* validation = cellValue.match(mailReg); if (validation != *null*) { finalData.push({ id: recordId, valuesMap: { [checkFieldId]: true } });
  }
} if (finalData.length) { *await* datasheet.updateRecordsAsync(finalData); } output.text('Complete the check!!!')
Previous « Data matcher Developer Center Development guide API Reference Social Twitter More Homepage Help Center GitHub Next Find the id card number in a column »