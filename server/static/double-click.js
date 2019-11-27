$(() => {
  const $tasksList = $('#tasks-list');
  const $idText = $('#id_text');
  let textClasses;
  let textId;
  let textValue;

  const protectFromScript = originalInputValue => {
    let newInputValue = String(originalInputValue);

    newInputValue = newInputValue.replace(/&/u, '&amp;')
      .replace(/</gu, '&lt;')
      .replace(/>/gu, '&gt;')
      .replace(/"/gu, '&quot;')
      .replace(/'/gu, '&apos;')
      .replace(/\//gu, '&frasl;')
      .replace(/\$/gu, '&#36;')
      .replace(/\[/gu, '&#91;')
      .replace(/\]/gu, '&#93;')
      .replace(/\{/gu, '&#123;')
      .replace(/\}/gu, '&#125;')
      .replace(/ {1,}/gu, ' ');

    return newInputValue;
  };

  $tasksList.on('dblclick', '.task-text', function() {
    textId = $(this).attr('id');
    textClasses = $(this).attr('class');
    textValue = protectFromScript($(this).text());
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

