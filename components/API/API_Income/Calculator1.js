import React, { useState } from 'react';
import axios from 'axios';

const Calculator1 = () => {
  const [salary, setSalary] = useState('');
  const [zip_code, setZipcode] = useState('');
  const [job_title, setJobtitle] = useState('');
  const [output, setOutput] = useState(null);
  console.log('response1');
  const calculateOutcome = async () => {
    try {
    console.log('response');
//      const response = await axios.get(`http://localhost:8080/calculator2?stated_gross_income=${salary}&zip_code=${zip_code}&job_title=${job_title}`);
      const response = await axios.get(`https://landing-page2-odv8wckiz-mohammads-projects-797ddea3.vercel.app/api/calculator2?stated_gross_income=${salary}&zip_code=${zip_code}&job_title=${job_title}
`);
      console.log(response);
      setOutput(response.data); // Set the entire JSON object

    } catch (error) {
      console.error('Error calculating outcome:', error);
    }
  };

  return (
    <div>
      <input
        type="number"
        placeholder="Salary"
        value={salary}
        onChange={(e) => setSalary(e.target.value)}
      />
      <input
        type="string"
        placeholder="ZIP Code"
        value={zip_code}
        onChange={(e) => setZipcode(e.target.value)}
      />
      <input
        type="string"
        placeholder="Job Title"
        value={job_title}
        onChange={(e) => setJobtitle(e.target.value)}
      />
      <button onClick={calculateOutcome}>Submit</button>
      {output && (
        <pre className="code-block">
          {JSON.stringify(output, null, 2)}
        </pre>
      )}
    </div>
  );
};

export default Calculator1;
