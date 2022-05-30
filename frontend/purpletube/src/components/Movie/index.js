import React from "react";
import "./style.css";
function Movie({id}) {
  return <div className="movie-card">
      <img src='https://m.media-amazon.com/images/M/MV5BMTk5NjkyNzEwOV5BMl5BanBnXkFtZTcwODc5NDI1MQ@@._V1_SX300.jpg'/>
        <p>84min</p>
    </div>;
}
export default Movie;
