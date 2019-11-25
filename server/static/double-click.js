$(() => {
  const $tasksList = $('#tasks-list');
  const $idText = $('#id_text');
  let textClasses;
  let textId;
  let textValue;

  $tasksList.on('dblclick', '.task-text', function() {
    textId = $(this).attr('id');
    textClasses = $(this).attr('class');
    textValue = $(this).text();
    $(this).replaceWith(`<form class="col-md-10" id="edit-form" 
    action="/editTodo/${$(this).attr('id')}" method = "POST">
    <input type="hidden" name="csrfmiddlewaretoken"
    value="USEotQ7iq8evVn8SasemdZNcYAOL1fLCPHdsDjyFExCrzCt5eH6UBaP2SjGbBOea">
    <input type="text" class='form-control col-md-12' 
    id='edit-form-id' name="edit-text" value='${$(this).text()}'>
    </form>`);
    $('#edit-form-id').focus();
  });

  $(document).on('blur', '#edit-form-id', function() {
    $(this).parent().replaceWith(`<span class="${textClasses}" id="${textId}">
    ${textValue}</span>`);
    $idText.focus();
  });
});

