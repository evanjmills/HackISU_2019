import React from 'react';

export const Leaderboard = () => (
  <div className='leaderboard-wrapper'>
    <div className='leaderboard'>
      <h2>Leaderboard</h2>
      <table cellSpacing='0'>
        <thead>
          <th>Rank</th>
          <th>Name</th>
          <th>Score</th>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>name1</td>
            <td>1</td>
          </tr>
          <tr>
            <td>2</td>
            <td>name2</td>
            <td>2</td>
          </tr>
          <tr>
            <td>3</td>
            <td>name3</td>
            <td>3</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
);
