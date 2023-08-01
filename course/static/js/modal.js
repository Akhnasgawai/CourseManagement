// JavaScript to show the delete confirmation modal
function showDeleteConfirmationModal(course_id, type) {
    document.getElementById("deleteModal").style.display = "block";
    window.courseId = [type, course_id];
    console.log(window.courseId)
}
  
// JavaScript to close the delete confirmation modal
function closeDeleteConfirmationModal() {
    document.getElementById("deleteModal").style.display = "none";
}
  
// JavaScript to handle the delete operation
function deleteItem() {
    course_id = window.courseId[1]
    closeDeleteConfirmationModal();
    if(window.courseId[0] === 'course'){
        closeDeleteConfirmationModal();
        window.location.href = `http://127.0.0.1:8000/delete-course/?course_id=${course_id}`
    }
    else{
        closeDeleteConfirmationModal();
        window.location.href = `http://127.0.0.1:8000/delete-content/?content_id=${course_id}`
    }
    
}
  