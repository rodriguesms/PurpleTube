import React, { useEffect, useState } from "react";
import { Star, Clock } from "react-feather";
import { api } from "../../services/api";
import "./style.css";
function Movie({ id, duration, banner }) {
  const [avaliations, setAvaliations] = useState();

  useEffect(() => {
    api.get(`avaliations/movie_media_avaliation/${id}`).then((response) => {
      setAvaliations(response.data.media);
    });
  }, []);
  return (
    <div className="movie-card">
      <img src={String(banner)} />
      <div className="movie-info">
        <span>
          <Star size={20} />
          <p>{avaliations}/10</p>
        </span>
        <span>
          <Clock size={20} />
          <p>{duration}</p>
        </span>
      </div>
    </div>
  );
}
export default Movie;
