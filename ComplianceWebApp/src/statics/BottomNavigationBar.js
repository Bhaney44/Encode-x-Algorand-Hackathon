import React from "react";
import {Link} from 'react-router-dom';

const BottomNavigationBar = ({txt}) => {
 

  return (
    <footer className="ft_sm">
      {
        txt === 'Check schedule?' ?  
        (<Link to='/schedule'>
        <p className="para">{txt} </p>
      </Link>) : (<Link to='/'>
        <p className="para"> {txt} </p>
      </Link>)
      }
     
      
    </footer>
  );
};

export default BottomNavigationBar;
