import React from 'react';
import clsx from 'clsx';
import styles from './DiagramContainer.module.css';

/**
 * Component for displaying diagrams in the Physical AI textbook
 * @param {Object} props - Component properties
 * @param {string} props.title - Title of the diagram
 * @param {string} props.type - Type of diagram (mermaid, conceptual, 3d-model)
 * @param {string} props.description - Textual description of the diagram content
 * @param {string} [props.content] - Mermaid syntax or description of the diagram
 * @param {string} [props.imageUrl] - Path to static image if applicable
 */
const DiagramContainer = ({ title, type, description, content, imageUrl }) => {
  const renderDiagram = () => {
    if (type === 'mermaid' && content) {
      // For mermaid diagrams, we'll render the content as a code block that Docusaurus will transform
      return (
        <div className="language-mermaid">
          <pre><code className="language-mermaid">{content}</code></pre>
        </div>
      );
    } else if (imageUrl) {
      return <img src={imageUrl} alt={description} className={styles.diagramImage} />;
    }
    return <div className={styles.diagramPlaceholder}>{description}</div>;
  };

  return (
    <div className={clsx('card', styles.diagramContainer)}>
      <div className="card__header">
        <h3 className={styles.diagramTitle}>{title}</h3>
        <span className={styles.typeBadge}>{type}</span>
      </div>
      <div className="card__body">
        <div className={styles.diagramContent}>
          {renderDiagram()}
        </div>
        <div className={styles.diagramDescription}>
          <p>{description}</p>
        </div>
      </div>
    </div>
  );
};

export default DiagramContainer;