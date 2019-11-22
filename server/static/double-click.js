$(() => {
  const $tasksList = $('#tasks-list');
  const $idText = $('#id_text');

  $tasksList.on('dblclick', '.task-text', function() {
    $(this).replaceWith(`<input type='text' class='form-control col-md-8' 
    id='edit-form-id' value='${$(this).text()}'>
    <input type="submit" value="+">`);
    $('#edit-form-id').focus();
  });

  $(document).on('blur', '#edit-form-id', () => {
    $idText.focus();
  });
});
