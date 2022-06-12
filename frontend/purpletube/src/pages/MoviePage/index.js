import React from "react";
import "./style.css";
import { useLocation } from 'react-router-dom';
import { TopBar } from '../../components/TopBar'

function MoviePage() {

  const movie = useLocation().state.movie

   return (
    <div className="pageContainer">
      <div className="topBar">
        <TopBar isHome={false} />
      </div>
      <div className="body">
      </div>
    </div>
  );
}
export default MoviePage;
