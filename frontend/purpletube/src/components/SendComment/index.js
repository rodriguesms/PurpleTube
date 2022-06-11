import "./style.css";
import { MessageSquare } from "react-feather";
import { api } from "../../services/api";
import { useState } from "react";

function SendComment({ codigo_usuario, codigo_filme }) {
  const [comment, setComment] = useState();
  function handleChange(event) {
    const { value } = event.target;
    setComment(value);
  }
  function handleSubmit(event) {
    event.preventDefault();
    const json_string = JSON.stringify({
      codigo_usuario: codigo_usuario,
      codigo_filme: codigo_filme,
      "conteudo": "ótimo"
    });
    console.log(json_string);
    api.post("comments", json_string).then((response) => {
      console.log(response);
    });
  }

  return (
    <form className="commentContainer" onSubmit={handleSubmit}>
      <input id="sendComment" type="text" />
      <button id="buttonComment" onChange={handleChange}>
        <MessageSquare /> Comentar
      </button>
    </form>
  );
}
export default SendComment;
