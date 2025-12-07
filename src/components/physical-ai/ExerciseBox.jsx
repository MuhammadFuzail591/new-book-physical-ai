import React from 'react';
import clsx from 'clsx';
import styles from './ExerciseBox.module.css';

// Define the Exercise component based on the contract
const Exercise = ({ title, description, difficulty, type, solution, hints }) => {
  const [showSolution, setShowSolution] = React.useState(false);
  const [showHints, setShowHints] = React.useState(false);

  const getDifficultyColor = (difficulty) => {
    switch (difficulty.toLowerCase()) {
      case 'beginner':
        return '#4caf50'; // Green
      case 'intermediate':
        return '#ff9800'; // Orange
      case 'advanced':
        return '#f44336'; // Red
      default:
        return '#9e9e9e'; // Gray
    }
  };

  const getTypeIcon = (type) => {
    switch (type.toLowerCase()) {
      case 'theoretical':
        return '📖';
      case 'practical':
        return '🔧';
      case 'coding':
        return '💻';
      case 'analysis':
        return '📊';
      default:
        return '❓';
    }
  };

  return (
    <div className={clsx('exercise-box', styles.exerciseBox)}>
      <div className={styles.header}>
        <div className={styles.titleRow}>
          <h3 className={styles.title}>{title}</h3>
          <span
            className={styles.difficultyBadge}
            style={{ backgroundColor: getDifficultyColor(difficulty) }}
          >
            {difficulty}
          </span>
          <span className={styles.typeIcon} title={type}>
            {getTypeIcon(type)}
          </span>
        </div>
      </div>

      <div className={styles.description}>
        <p>{description}</p>
      </div>

      <div className={styles.actions}>
        {hints && hints.length > 0 && (
          <button
            className={clsx('button button--secondary button--sm', styles.hintButton)}
            onClick={() => setShowHints(!showHints)}
          >
            {showHints ? 'Hide Hints' : 'Show Hints'}
          </button>
        )}

        {solution && (
          <button
            className={clsx('button button--primary button--sm', styles.solutionButton)}
            onClick={() => setShowSolution(!showSolution)}
          >
            {showSolution ? 'Hide Solution' : 'Show Solution'}
          </button>
        )}
      </div>

      {showHints && hints && hints.length > 0 && (
        <div className={clsx('alert alert--info', styles.hints)}>
          <h4>Hints:</h4>
          <ul>
            {hints.map((hint, index) => (
              <li key={index}>{hint}</li>
            ))}
          </ul>
        </div>
      )}

      {showSolution && solution && (
        <div className={clsx('alert alert--success', styles.solution)}>
          <h4>Solution:</h4>
          <p>{solution}</p>
        </div>
      )}
    </div>
  );
};

export default Exercise;