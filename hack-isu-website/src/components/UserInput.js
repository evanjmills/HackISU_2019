import React from 'react';

export const UserInput = () => (
  <div className='user-input-wrapper'>
    <div className='user-input'>
      <h2>Make A Choice</h2>
      <form>
        <div>
          <label htmlFor='name'>Name</label>
          <input type='text' name='name' id='' />
        </div>
        <div className='user-options-wrapper'>
          <div>
            <label htmlFor='numHidden'>numHidden</label>
            <input type='text' name='numHidden' id='' />
          </div>
          <div>
            <label htmlFor='survival'>survival</label>
            <input type='text' name='survival' id='' />
          </div>
          <div>
            <label htmlFor='nodeAdd'>nodeAdd</label>
            <input type='text' name='nodeAdd' id='' />
          </div>
          <div>
            <label htmlFor='nodeDel'>nodeDel</label>
            <input type='text' name='nodeDel' id='' />
          </div>
          <div>
            <label htmlFor='connAdd'>connAdd</label>
            <input type='text' name='connAdd' id='' />
          </div>
          <div>
            <label htmlFor='connDel'>connDel</label>
            <input type='text' name='connDel' id='' />
          </div>
          <div>
            <label htmlFor='weightAdd'>weightAdd</label>
            <input type='text' name='weightAdd' id='' />
          </div>
          <div>
            <label htmlFor='weightDel'>weightDel</label>
            <input type='text' name='weightDel' id='' />
          </div>
        </div>
      </form>
    </div>
  </div>
);
