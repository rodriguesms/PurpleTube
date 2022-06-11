import { useState, useEffect } from "react";
import DisplayComment from "../../components/DisplayComment";
import SendComment from "../../components/SendComment";
import { api } from "../../services/api";
function TestComment() {
  const codigo_filme = 5;
  const [comments, setComments] = useState();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get(`comments/movie_comments/${codigo_filme}`).then((response) => {
      setComments(response.data);
      setLoading(false);
    });
  }, []);
  return (
    <div>
      <SendComment codigo_usuario={1} codigo_filme={5} />
      {!loading &&
        comments.map((comment) => (
          <DisplayComment
            user={String(comment.codigo_usuario)}
            comment={comment.conteudo}
            date={comment.data}
          />
        ))}
    </div>
  );
}
export default TestComment;
