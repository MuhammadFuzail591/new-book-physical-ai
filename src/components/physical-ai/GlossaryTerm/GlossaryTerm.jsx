import React from 'react';
import clsx from 'clsx';
import styles from './GlossaryTerm.module.css';

/**
 * Component for displaying glossary terms in the Physical AI textbook
 * @param {Object} props - Component properties
 * @param {string} props.term - The technical term
 * @param {string} props.definition - Definition of the term
 * @param {Array<string>} [props.usageExamples] - Examples of how the term is used
 * @param {Array<string>} [props.relatedTerms] - Related terms in the glossary
 */
const GlossaryTerm = ({ term, definition, usageExamples = [], relatedTerms = [] }) => {
  return (
    <div className={clsx('card', styles.glossaryTerm)}>
      <div className="card__header">
        <h3 className={styles.termTitle}>{term}</h3>
      </div>
      <div className="card__body">
        <div className={styles.definition}>
          <p><strong>Definition:</strong> {definition}</p>
        </div>

        {usageExamples.length > 0 && (
          <div className={styles.usageExamples}>
            <strong>Usage Examples:</strong>
            <ul>
              {usageExamples.map((example, index) => (
                <li key={index} className={styles.exampleItem}>{example}</li>
              ))}
            </ul>
          </div>
        )}

        {relatedTerms.length > 0 && (
          <div className={styles.relatedTerms}>
            <strong>Related Terms:</strong>
            <ul>
              {relatedTerms.map((term, index) => (
                <li key={index} className={styles.relatedTermItem}>
                  <a href={`#`} onClick={(e) => e.preventDefault()}>{term}</a>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default GlossaryTerm;