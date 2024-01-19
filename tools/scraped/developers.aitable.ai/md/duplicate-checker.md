Search Getting StartedExamplesLink records with duplicate values On this page

## Link Records With Duplicate Values

INFO
Select a record and the column to be checked, the script will automatically find the rest of the duplicate records and then associate them to the selected record (you need to create a Two-way link field in advance)

## Demo Source Code

 datasheet =  space.getActiveDatasheetAsync(); storeField =  input.fieldAsync(
  "Please select the field to store duplicate records, the type needs to be two-way link and the association is the curre
  datasheet ); if (storeField.type != "TwoWayLink") { output.text( "Failed to run: The selected field type needs to be a Two-way link" ); } *else* if (storeField.property.foreignDatasheetId != datasheet.id) { output.text(
    "Failed to run: the selected magical link field must be linked to current datasheet" ); } *else* { console.log(storeField.property); *const* needFindRecord = *await* input.recordAsync( "Please select the record to check:", datasheet ); *const* needFindField = *await* input.fieldAsync( "Please select the fields to check for duplicates:", datasheet );
  *const* records = *await* datasheet.getRecordsAsync(); // Define two data sets that need to be used later, duplicates stores the duplicate record ids found, and valuesMap wil *const* duplicates = []; *const* valuesMap = {}; for (let record of records) { //The data that is empty does not belong to the content to be found, so it is skipped if (record.getCellValueString(needFindField.id) === *null*) { *continue*; } //Need to exclude yourself when checking for duplicates if (record.id === needFindRecord.id) { *continue*; } //Obtain data according to getCellValueString and judge whether they are equal. If they are equal, it means that the if ( record.getCellValueString(needFindField.id) === needFindRecord.getCellValueString(needFindField.id) ) { duplicates.push(record.id); } } console.log(duplicates); if (duplicates.length === 0) {
    output.text(`No duplicate records found`);
  } *else* { output.text( `Found ${duplicates.length} duplicate records, which have been linked in the Two-way link field` ); valuesMap[storeField.id] = duplicates; *await* datasheet.updateRecordAsync(needFindRecord.id, valuesMap); } }
Previous « Find the phone number in a column Developer Center Development guide API Reference Social Twitter More Extract URL from attachment »
© 2023 AITable Ltd. All rights reserved.