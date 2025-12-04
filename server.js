require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { sequelize } = require('./src/config/database');
const { User, Project } = require('./src/models');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Initialize database with demo users
const initializeDatabase = async () => {
  try {
    await sequelize.sync({ force: true });
    console.log('✓ Database synchronized');

    // Create demo users
    const student = await User.create({
      email: 'student@ucu.ac.ug',
      password: 'password123',
      full_name: 'Sserunkuma Michael',
      role: 'student',
      faculty: 'Faculty of Science and Technology',
      year: 3
    });

    const supervisor = await User.create({
      email: 'supervisor@ucu.ac.ug',
      password: 'password123',
      full_name: 'Dr. Matovu Benjamin',
      role: 'supervisor',
      faculty: 'Faculty of Science and Technology'
    });

    const admin = await User.create({
      email: 'admin@ucu.ac.ug',
      password: 'password123',
      full_name: 'Omiya Arnold Will',
      role: 'admin'
    });

    console.log('✓ Demo users created');
  } catch (err) {
    console.error('Database initialization error:', err.message);
  }
};

// Initialize database on startup
initializeDatabase();

// Routes
try {
  app.use('/api/auth', require('./src/routes/auth'));
  app.use('/api/users', require('./src/routes/users'));
  app.use('/api/projects', require('./src/routes/projects'));
  app.use('/api/comments', require('./src/routes/comments'));
  app.use('/api/analytics', require('./src/routes/analytics'));
} catch (err) {
  console.error('Error loading routes:', err.message);
}

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(500).json({ error: err.message || 'Internal server error' });
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Backend server running on port ${PORT}`);
});
