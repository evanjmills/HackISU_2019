import React from 'react';

export const UserInput = () => (
  <div className='userinput'>
    <h2>Make A Choice</h2>
    <form action=''>
      <div>
        <label htmlFor='name'>Name</label>
        <input type='text' name='name' id='' />
      </div>
      <div>
        <label htmlFor='param1'>Param1</label>
        <input type='text' name='param1' id='' />
      </div>
      <div>
        <label htmlFor='param2'>Param2</label>
        <input type='text' name='param2' id='' />
      </div>
      <div>
        <label htmlFor='param3'>Param3</label>
        <input type='text' name='param3' id='' />
      </div>
      <div>
        <label htmlFor='param4'>Param4</label>
        <input type='text' name='param4' id='' />
      </div>
      <div>
        <label htmlFor='param5'>Param5</label>
        <input type='text' name='param5' id='' />
      </div>
    </form>
  </div>
);
