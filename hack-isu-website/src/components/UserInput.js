import React from 'react';

const handleSubmit = e => {
  e.preventDefault();
  const data = new FormData(e.target);

  fetch('https://neat-ouybuaq47q-uc.a.run.app:8080', {
    method: 'POST',
    body: data
  });
};

export const UserInput = () => (
  <div className='user-input-wrapper'>
    <div className='user-input'>
      <h2>Make A Choice</h2>
      <form onSubmit={e => handleSubmit(e)}>
        <div>
          <label htmlFor='name'>Name</label>
          <input type='text' name='name' id='' />
        </div>
        <div className='user-options-wrapper'>
          <div>
            <label htmlFor='num_hidden'>Number Hidden</label>
            <input type='text' name='num_hidden' id='' />
          </div>
          <div>
            <label htmlFor='survival'>Survival Rate</label>
            <input type='text' name='survival' id='' />
          </div>
          <div>
            <label htmlFor='node_add_prob'>Node Add Prob.</label>
            <input type='text' name='node_add_prob' id='' />
          </div>
          <div>
            <label htmlFor='node_del_prob'>Node Delete Prob.</label>
            <input type='text' name='node_del_prob' id='' />
          </div>
          <div>
            <label htmlFor='conn_add_prob'>Connection Add Prob.</label>
            <input type='text' name='conn_add_prob' id='' />
          </div>
          <div>
            <label htmlFor='conn_del_prob'>Connection Delete Prob.</label>
            <input type='text' name='conn_del_prob' id='' />
          </div>
          <div>
            <label htmlFor='weight_mutate_rate'>Weight Mutate Prob.</label>
            <input type='text' name='weight_mutate_rate' id='' />
          </div>
          <div>
            <label htmlFor='weight_replace_rate'>Weight Replace Prob.</label>
            <input type='text' name='weight_replace_rate' id='' />
          </div>
        </div>
        <input type='submit' value='Try It Out!' />
      </form>
    </div>
  </div>
);
