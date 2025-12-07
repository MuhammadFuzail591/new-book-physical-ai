import React from 'react';
import clsx from 'clsx';
import styles from './CodeExample.module.css';

/**
 * Component for displaying code examples in the Physical AI textbook
 * @param {Object} props - Component properties
 * @param {string} props.title - Title of the code example
 * @param {string} props.language - Programming language or format (python, bash, xml, etc.)
 * @param {string} props.code - The actual code content
 * @param {string} props.description - Explanation of what the code does
 * @param {string} [props.environment] - Target environment for execution
 * @param {string} [props.executionInstructions] - Step-by-step instructions to run the code
 */
const CodeExample = ({ title, language, code, description, environment, executionInstructions }) => {
  return (
    <div className={clsx('card', styles.codeExample)}>
      <div className="card__header">
        <h3 className={styles.codeTitle}>{title}</h3>
        <span className={styles.languageBadge}>{language}</span>
      </div>
      <div className="card__body">
        <div className={styles.codeDescription}>
          <p>{description}</p>
        </div>

        <div className={styles.codeBlock}>
          <pre>
            <code className={clsx('language-', language)}>
              {code}
            </code>
          </pre>
        </div>

        {environment && (
          <div className={styles.environmentInfo}>
            <strong>Environment:</strong> {environment}
          </div>
        )}

        {executionInstructions && (
          <div className={styles.executionInstructions}>
            <strong>Execution Instructions:</strong>
            <div className={styles.instructionsContent}>
              {executionInstructions}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default CodeExample;