$(() => {
  const $tasksList = $('#tasks-list');
  const $idText = $('#id_text');
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
      .replace(/ {1,}/gu, ' ')
      .trim();

    return newInputValue;
  };

  $tasksList.on('dblclick', '.task-text', function() {
    textValue = protectFromScript($(this).text());
    $(this).addClass('hide');
    $(this).next().removeClass('hide');
    $('#id_edit_text').focus();
    $('#id_edit_text').val(textValue);
  });

  $(document).on('blur', '#id_edit_text', function() {
    $(this).parent().addClass('hide');
    $(this).parent().prev().removeClass('hide');
    $idText.focus();
  });
});

