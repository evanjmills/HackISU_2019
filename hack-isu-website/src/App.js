import React from 'react';
import logo from './logo.svg';
import './App.scss';
import { Descriptions } from './components/Descriptions';
import { Leaderboard } from './components/Leaderboard';
import { Video } from './components/Video';
import { UserInput } from './components/UserInput';

function App() {
  return (
    <div className='App'>
      <h1 className='header'>
        A <span>NEAT</span> Way to Play
      </h1>
      <Video />
      <Descriptions />
      <Leaderboard />
      <UserInput />
    </div>
  );
}

export default App;
