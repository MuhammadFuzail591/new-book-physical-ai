import React from 'react';
import clsx from 'clsx';
import styles from './ExerciseBox.module.css';

/**
 * Component for displaying exercises in the Physical AI textbook
 * @param {Object} props - Component properties
 * @param {string} props.title - Title of the exercise
 * @param {string} props.description - Detailed description of the exercise
 * @param {string} props.difficulty - Difficulty level (beginner, intermediate, advanced)
 * @param {string} props.type - Type of exercise (theoretical, practical, coding, analysis)
 * @param {string} [props.solution] - Solution or expected outcome
 * @param {Array<string>} [props.hints] - Helpful hints for solving the exercise
 */
const ExerciseBox = ({ title, description, difficulty, type, solution, hints = [] }) => {
  const getDifficultyColor = (difficulty) => {
    switch (difficulty?.toLowerCase()) {
      case 'beginner':
        return 'beginner';
      case 'intermediate':
        return 'intermediate';
      case 'advanced':
        return 'advanced';
      default:
        return 'beginner';
    }
  };

  const getTypeLabel = (type) => {
    switch (type?.toLowerCase()) {
      case 'theoretical':
        return 'Theoretical';
      case 'practical':
        return 'Practical';
      case 'coding':
        return 'Coding';
      case 'analysis':
        return 'Analysis';
      default:
        return type;
    }
  };

  return (
    <div className={clsx('card', styles.exerciseBox, styles[getDifficultyColor(difficulty)])}>
      <div className="card__header">
        <h3 className={styles.exerciseTitle}>
          <span className={clsx(styles.difficultyBadge, styles[getDifficultyColor(difficulty)])}>
            {difficulty}
          </span>
          {title}
        </h3>
        <span className={styles.exerciseType}>{getTypeLabel(type)}</span>
      </div>
      <div className="card__body">
        <div className={styles.exerciseDescription}>
          <p>{description}</p>
        </div>

        {hints.length > 0 && (
          <div className={styles.hintsSection}>
            <h4>Hints:</h4>
            <ul>
              {hints.map((hint, index) => (
                <li key={index} className={styles.hintItem}>{hint}</li>
              ))}
            </ul>
          </div>
        )}

        {solution && (
          <details className={styles.solutionSection}>
            <summary>Solution</summary>
            <div className={styles.solutionContent}>
              {solution}
            </div>
          </details>
        )}
      </div>
    </div>
  );
};

export default ExerciseBox;