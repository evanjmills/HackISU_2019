import React from 'react';

export const Descriptions = () => (
  <div className='descriptions-wrapper'>
    <div className='descriptions'>
      {/* <h2>Your Options - Explained</h2> */}
      <div>
        <h3>Number Hidden</h3>
        <p>Total number of hidden nodes.</p>
      </div>
      <div>
        <h3>Node Add Probability</h3>
        <p>Probability that a hidden node is added to the model.</p>
      </div>
      <div>
        <h3>Connection Add Probability</h3>
        <p>
          Probability that a new connection is added between existing nodes.
        </p>
      </div>
      <div>
        <h3>Weight Mutation Rate</h3>
        <p>Probability that a random connection weight will be mutated.</p>
      </div>
      <div>
        <h3>Survival Rate</h3>
        <p>
          Percentage of a species that survives from one generation to the next.
        </p>
      </div>
      <div>
        <h3>Node Delete Probability</h3>
        <p>Probability that a hidden node is deleted from the model.</p>
      </div>

      <div>
        <h3>Connection Delete Probability</h3>
        <p>
          Probability that an existing connection is deleted between existing
          nodes.
        </p>
      </div>

      <div>
        <h3>Weight Replacement Rate</h3>
        <p>Probability that a random connection weight will be replaced.</p>
      </div>
    </div>
  </div>
);
