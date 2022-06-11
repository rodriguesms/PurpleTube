
import './style.css'
function DisplayComment({ user, comment,date }) {

  return (
    <div className="comment">
      <p id="user">{user} <span id="date">{date}</span></p>
      <p id="comment">{comment}</p>
   </div>
  );
}
export default DisplayComment;
