import React from 'react';
import clsx from 'clsx';
import styles from './CodeExample.module.css';

// Define the CodeExample component based on the contract
const CodeExample = ({ title, language, code, description, environment, executionInstructions }) => {
  const [showInstructions, setShowInstructions] = React.useState(false);

  return (
    <div className={clsx('code-example', styles.codeExample)}>
      <div className={styles.header}>
        <h3 className={styles.title}>{title}</h3>
        <span className={styles.languageTag}>Language: {language}</span>
      </div>

      {description && (
        <div className={styles.description}>
          <p>{description}</p>
        </div>
      )}

      <div className={styles.codeContainer}>
        <pre className={styles.codeBlock}>
          <code className={`language-${language}`}>
            {code}
          </code>
        </pre>
      </div>

      {environment && (
        <div className={clsx('alert alert--info', styles.environment)}>
          <strong>Environment:</strong> {environment}
        </div>
      )}

      {executionInstructions && (
        <div className={styles.instructions}>
          <button
            className={clsx('button button--secondary button--sm', styles.instructionsButton)}
            onClick={() => setShowInstructions(!showInstructions)}
          >
            {showInstructions ? 'Hide Instructions' : 'Show Execution Instructions'}
          </button>

          {showInstructions && (
            <div className={clsx('alert alert--secondary', styles.instructionsContent)}>
              <h4>Execution Instructions:</h4>
              <p>{executionInstructions}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default CodeExample;