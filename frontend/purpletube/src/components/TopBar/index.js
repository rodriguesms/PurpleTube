import React, {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import { Film, User, LogIn, Search } from 'react-feather';
import { Button } from '@material-ui/core';
import { useNavigate } from 'react-router-dom';
import './style.css';

export const TopBar = () => {
  
  const [user, setUser] = useState();
  const [isLogged, setLogged] = useState(false);
  const [loadingUser, setLoadingUser] = useState(true);
  const navigate = useNavigate()

  useEffect(() => {
    let loadUser = localStorage.getItem('user');
    if(loadUser){
      setLogged(true);
      setUser(JSON.parse(loadUser));
    }
    setLoadingUser(false);
  }, [])

  return(
  <div className="container">
    <Link to="/" className="homeTitle">
      <Film style={{ marginRight: "15px"}} />
      PurpleTube
    </Link>
    <div className="searchBar">
      <div className="barContainer">
        <input type="text" className="inputSearch"/>
        <Button>
          <Search color='#CFCFCF'/>
        </Button>
      </div>
    </div>
    <div className="userSection">
      {
        (!loadingUser && (
          !isLogged && <Button onClick={() => navigate('/login')} className="profile">
            <LogIn style={{marginRight: '20px'}}/>
            Login</Button>
        )) || (!loadingUser && (
          isLogged && <Button className="profile">
            <User style={{marginRight: '20px'}}/> 
            {user.nome_usuario}
          </Button>
        )) 
      }
    </div>
  </div>
  )
}