import "./style.css";
import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { MessageSquare } from "react-feather";
import { api } from "../../services/api";
import { useState } from "react";

function SendComment({ codigo_usuario, codigo_filme }) {
  const [comment, setComment] = useState("");
  const navigate = useNavigate();
  function handleToMoviePage() {
    api.get(`movies/movie_id/${codigo_filme}`).then((responseMovie) => {
      navigate("/movie", { state: { movie: responseMovie.data } });
    });
  }
  function handleSubmit(event) {
    event?.preventDefault();
    console.log("comment", codigo_usuario, codigo_filme, comment);
    api
      .post("comments", {
        codigo_usuario: codigo_usuario,
        codigo_filme: codigo_filme,
        conteudo: comment,
      })
      .then((response) => {
        console.log(response);

        if (response.ok) {
          handleToMoviePage()
          return response.json();
          
        }
        throw response;
      })
      /*.then((data) => {
        fetchComments();
      })*/
      .catch((error) => {
        console.log(error);
      })

  }

  return (
    <form className="commentContainer">
      <input
        id="sendComment"
        type="text"
        onChange={(e) => setComment(e.target.value)}
      />
      <button id="buttonComment" onClick={handleSubmit}>
        <MessageSquare /> Comentar
      </button>
    </form>
  );
}
export default SendComment;
