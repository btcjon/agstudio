Search Getting StartedExamplesFind and replace On this page

## Find And Replace

INFO
Supports finding and replacing specified text in specified fields

## Demo Source Code

const findText = *await* input.textAsync( "Please enter the text you want to find:" );
const replaceText = *await* input.textAsync(
  "Want to replace the find text with:" ); // The currently active form needs to be obtained through the Space API and passed to input.fieldAsync as a parameter const datasheet = *await* space.getActiveDatasheetAsync(); const field = *await* input.fieldAsync( "Please select the field name you want to find", datasheet
); // Get the id of field const fieldId = field.id; const records = *await* datasheet.getRecordsAsync(); const finalData = []; // traverse records for (let record of records) { *const* recordId = record.id; // Get the data of the specified field of the record as cellValue *const* cellValue = record.getCellValueString(fieldId);
  // If the acquired data is empty, jump out of this cycle and directly execute the next time
  if (cellValue == null) *continue*; // Replace findText in cellValue with replaceText, and use a new variable - newCellValue *const* newCellValue = cellValue.replaceAll(findText, replaceText); // Determine whether the data before replacement is consistent with the data after replacement if (cellValue !== newCellValue) { // Inconsistency means that the corresponding record in the table needs to replace cellValue with newCellValue, and t finalData.push({ id: recordId, valuesMap: { [fieldId]: newCellValue }, }); } } // Determine whether there is data in finalData, if there is no data, there is no need to replace if (finalData.length) { *await* datasheet.updateRecordsAsync(finalData); output.text("The replacement is complete!"); } *else* { output.text("No data found to be replaced"); }
Previous « Code example Developer Center Development guide API Reference Social Twitter More Homepage Help Center GitHub Next Data matcher »