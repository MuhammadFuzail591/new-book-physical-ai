import React from 'react';
import clsx from 'clsx';
import styles from './GlossaryTerm.module.css';

// Define the GlossaryTerm component based on the contract
const GlossaryTerm = ({ term, definition, usageExamples, relatedTerms }) => {
  const [expanded, setExpanded] = React.useState(false);

  return (
    <div className={clsx('glossary-term', styles.glossaryTerm)}>
      <div className={styles.header}>
        <h4 className={styles.term}>
          <span className={styles.termText}>{term}</span>
        </h4>
        <button
          className={clsx('button button--secondary button--sm', styles.expandButton)}
          onClick={() => setExpanded(!expanded)}
        >
          {expanded ? '▲' : '▼'}
        </button>
      </div>

      <div className={styles.definition}>
        <p>{definition}</p>
      </div>

      {expanded && (
        <div className={styles.details}>
          {usageExamples && usageExamples.length > 0 && (
            <div className={styles.examples}>
              <h5>Usage Examples:</h5>
              <ul>
                {usageExamples.map((example, index) => (
                  <li key={index}>{example}</li>
                ))}
              </ul>
            </div>
          )}

          {relatedTerms && relatedTerms.length > 0 && (
            <div className={styles.relatedTerms}>
              <h5>Related Terms:</h5>
              <ul>
                {relatedTerms.map((relatedTerm, index) => (
                  <li key={index} className={styles.relatedTerm}>
                    {relatedTerm}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default GlossaryTerm;