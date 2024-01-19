Search Getting StartedExamplesGenerate latitude and longitude from IP address On this page

## Generate Latitude And Longitude From Ip Address

INFO
Generate the latitude and longitude information of the area based on the IP address Demo Source code datasheet =  space.getActiveDatasheetAsync(); ipField =  input.fieldAsync( "Please select the field where the IP address is located:",
  datasheet
); const coordinateField = *await* input.fieldAsync( "Please select latitude and longitude to generate field:", datasheet ); // Define a dataset to store the data used to update the "latitude and longitude" column const finalData = [];
// Obtain coordinate information by IP address async *function* getCoordinateInfo(ip) { *const* res = *await* fetch(`https://ipwho.is/${ip}`); return *await* res.json(); } const ipFieldId = ipField.id; const coordinateFieldId = coordinateField.id; const records = datasheet.getRecordsAsync(); for (let record of records) { *const* recordId = record.id;
  let ip = record.getCellValue(ipFieldId);
  //The data that is empty does not belong to the content to be converted into latitude and longitude, so it is skipped if (ip == null) *continue*; *const* res = *await* getCoordinateInfo(ip); *const* coordinate = `${res.longitude}, ${res.latitude}`; // Add the data that needs to be updated to the finalData array finalData.push({ id: recordId, valuesMap: { [coordinateFieldId]: coordinate, }, }); } if (finalData.length) { *await* datasheet.updateRecordsAsync(finalData); } output.text("IP address has been converted to latitude and longitude!!!");
Previous « Extract URL from attachment Developer Center Development guide API Reference Social Twitter More Homepage Help Center GitHub Next Appendix: JavaScript Getting Started Guide »