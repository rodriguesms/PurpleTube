import React, { useState, useEffect } from "react";
import "./style.css";
import { useLocation } from 'react-router-dom';
import { TopBar } from '../../components/TopBar'
import { api } from "../../services/api";
import DisplayComment from '../../components/DisplayComment/index'
import SendComment from "../../components/SendComment";

function MoviePage() {

  const movie = useLocation().state.movie

  const [user, setUser] = useState();
  const [isLogged, setLogged] = useState(false);
  const [loadingUser, setLoadingUser] = useState(true);
  const [director, setDirector] = useState([""])
  const [actors, setActors] = useState([])
  const [loadDirector, setLoadDirector] = useState(true)
  const [loadActor, setLoadActor] = useState(true)
  const [comments, setComments] = useState([])
  const [loadComments, setLoadComments] = useState(true)

   useEffect(() => {

        let loadUser = localStorage.getItem('user');
        if(loadUser){
          setLogged(true);
          setUser(JSON.parse(loadUser));
        }
        setLoadingUser(false);

        api.get(`/actor/movie_actors/${movie.codigo_filme}`).then((response) => {
          setActors(response.data);
          setLoadActor(false);
        })

        api.get(`/directors/movie_directors/${movie.codigo_filme}`).then((response) => {
          setDirector(response.data);
          setLoadDirector(false);
        })

        api.get(`comments/movie_comments/${movie.codigo_filme}`).then((response) => {
          setComments(response.data)
          setLoadComments(false);
          console.log(comments)
        })
   }, []);

  
  return (
    <div className="pageContainer">
      <div className="topBar">
        <TopBar isHome={false}/>
      </div>
      <div className="body">
        <div className="mid-area">
          <div className="movieInfo-area">
            <div className="individual-movie-image-card">
              <img className="individual-movie-image" src={movie.baner}/>
            </div>
            <div className="mainMovieInfo">
              <div style={{display: "flex", flexDirection: "column", width: "100%", alignItems: "center"}}>
                <div className="movieTitle">{movie.nome_filme}</div>
                <div className="directors">
                  {
                    !loadDirector &&
                    director.map((director) => 
                      <div className="movieDirector" key={director.codigo_diretor}>{director.nome_diretor}</div>
                    )
                  } 
                </div>
              </div>
              <div className="movieDescription">{movie.descricao}</div>
              <div className="actorsDiv">
                {
                  !loadActor &&
                  actors.map((actor) => 
                    <div className="actors" key={actor.codigo_ator}>{actor.nome_ator}</div>
                  )
                }
              </div>
            </div>
          </div>
          <div className="comments-area">
            { isLogged && <SendComment codigo_filme={movie.codigo_filme} codigo_usuario={user.codigo_usuario}/> }
            {!loadComments && 
            comments.map((comment) => 
              <DisplayComment key={comment.codigo_comentario} 
              user={comment.nome_usuario} 
              comment={comment.conteudo}
              date={comment.data}/>
              )}
          </div>
        </div>
      </div>
    </div>
  );
}
export default MoviePage;
