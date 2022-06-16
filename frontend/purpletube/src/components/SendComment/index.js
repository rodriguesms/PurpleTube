import "./style.css";
import React, { useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import { MessageSquare } from "react-feather";
import { api } from "../../services/api";
import { useState } from "react";

function SendComment({ codigo_usuario, codigo_filme }) {
  const [comment, setComment] = useState("");
  const navigate = useNavigate()
  const d = new Date();

  function handleSubmit() {
    console.log(comment)
    api.post("comments", {
      codigo_usuario: codigo_usuario,
      codigo_filme: codigo_filme,
      date: `${d.getFullYear()}-${d.getMonth()}-${d.getDate()}`,
      conteudo: comment
    }).then((response) => {
      api.get(`movies/movie_id/${codigo_filme}`).then((responseMovie) => {
        navigate("/movie", { state: { movie: responseMovie.data}})
      })
    });
  }

  return (
    <form className="commentContainer" onSubmit={() => handleSubmit()}>
      <input id="sendComment" type="text" onChange={e => setComment(e.target.value)}/>
      <button id="buttonComment" >
        <MessageSquare /> Comentar
      </button>
    </form>
  );
}
export default SendComment;
