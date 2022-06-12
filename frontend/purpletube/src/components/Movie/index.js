import React, { useEffect, useState } from "react";
import { Star, Clock } from "react-feather";
import { api } from "../../services/api";
import { useNavigate } from 'react-router-dom';
import "./style.css";
function Movie({movie}) {

  const navigate = useNavigate()

  const goToMoviePage = () => {
    navigate("/movie", { state: { movie: movie}})
  }

  return (
    <div onClick={() => goToMoviePage()} className="movie-card">
      <img className="movie-image" src={movie.baner}/>
    </div>
  );
}
export default Movie;
