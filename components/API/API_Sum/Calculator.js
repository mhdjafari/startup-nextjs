import React, { useState } from 'react';
import axios from 'axios';

const Calculator = () => {
  const [number1, setNumber1] = useState('');
  const [number2, setNumber2] = useState('');
  const [sum, setSum] = useState(null);

  const calculateSum = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/calculate?x1=${number1}&x2=${number2}`);
      setSum(response.data.y);
      console.log(response.data.y)
    } catch (error) {
      console.error('Error calculating sum:', error);
    }
  };

  return (
    <div>
      <input
        type="number"
        placeholder="Enter number 1"
        value={number1}
        onChange={(e) => setNumber1(e.target.value)}
      />
      <input
        type="number"
        placeholder="Enter number 2"
        value={number2}
        onChange={(e) => setNumber2(e.target.value)}
      />
      <button onClick={calculateSum}>Calculate Sum</button>
      {sum && <p>Sum: {sum}</p>}
    </div>
  );
};

export default Calculator;
