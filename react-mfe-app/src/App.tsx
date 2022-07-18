import React from 'react';
import { ShellComponent, ErrorBoundaryWrapper } from 'ui';
import {ResearchPage} from "./pages/researchPage";
import './App.css';

function App() {
  
  return (
    <ErrorBoundaryWrapper>
      <ShellComponent title="Research">
        <h1>Ongoing Research Works</h1>
        <ResearchPage title={"Own Child"}/>
      </ShellComponent>
    </ErrorBoundaryWrapper>
  );
}

export default App;
