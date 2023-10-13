import axios from 'axios';

export default async function handler(req, res) {
  const { x1, x2 } = req.query;
  try {
    const response = await axios.get(
      `http://localhost:8000/calculate?x1=${x1}&x2=${x2}`
    );
    res.status(200).json({ sum: response.data.sum });
  } catch (error) {
    console.error('EEEEEEError calculating sum:', error);
    res.status(500).json({ error: 'EEEEError calculating sum' });
  }
}
