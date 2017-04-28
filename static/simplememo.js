function show_edit_dialog(id){
    var dialog = document.querySelector('#edit_dialog');
    var form = document.getElementById('edit_form');
    var edit_id = document.getElementById('edit_id');
    var edit_textarea = document.getElementById('edit_textarea');
    var ok_button = document.getElementById('dialog_edit_button');
    var cancel_button = document.getElementById('dialog_cancel_button');
    var memo = document.getElementById('memo_' + id);

    ok_button.addEventListener('click',function(){
        edit_id.value = id;
        form.submit();
        dialog.close();
    },false);

    cancel_button.addEventListener('click',function(){
        edit_textarea.value = "";
        dialog.close();
    },false);

    edit_textarea.value = memo.innerText;
    dialog.showModal();
    return false;
}

function show_delete_alert(id){
    var form = document.getElementById('delete_form_' + id);
    var memo_id = document.getElementById('memo_' + id + '_id');
    if(window.confirm("メモを削除してよろしいですか？")){
        memo_id.value = id;
        form.submit();
    }
    return false;
}
