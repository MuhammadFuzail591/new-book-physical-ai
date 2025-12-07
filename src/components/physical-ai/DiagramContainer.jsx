import React from 'react';
import clsx from 'clsx';
import styles from './DiagramContainer.module.css';

// Define the DiagramContainer component based on the contract
const DiagramContainer = ({ title, type, description, content, imageUrl }) => {
  const [showDetails, setShowDetails] = React.useState(false);

  const renderDiagram = () => {
    if (type === 'mermaid' && content) {
      // For Mermaid diagrams, we'll render the code and let Docusaurus handle it
      return (
        <div className={styles.mermaidContainer}>
          <pre className={styles.mermaidCode}>
            <code className="language-mermaid">{content}</code>
          </pre>
        </div>
      );
    } else if (imageUrl) {
      // For static images
      return (
        <div className={styles.imageContainer}>
          <img src={imageUrl} alt={description} className={styles.diagramImage} />
        </div>
      );
    } else if (content) {
      // For conceptual diagrams described in text
      return (
        <div className={styles.textDiagram}>
          <div className={styles.diagramContent}>{content}</div>
        </div>
      );
    }

    return (
      <div className={styles.placeholder}>
        <p>No diagram content provided</p>
      </div>
    );
  };

  return (
    <div className={clsx('diagram-container', styles.diagramContainer)}>
      <div className={styles.header}>
        <h3 className={styles.title}>{title}</h3>
        <span className={styles.typeTag}>{type}</span>
      </div>

      <div className={styles.diagramArea}>
        {renderDiagram()}
      </div>

      {description && (
        <div className={styles.description}>
          <button
            className={clsx('button button--secondary button--sm', styles.descriptionButton)}
            onClick={() => setShowDetails(!showDetails)}
          >
            {showDetails ? 'Hide Description' : 'Show Description'}
          </button>

          {showDetails && (
            <div className={clsx('alert alert--info', styles.descriptionContent)}>
              <p>{description}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default DiagramContainer;