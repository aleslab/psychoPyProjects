#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Wed May 13 16:21:28 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'AP'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ales/psychoPyProjects/pikiou/AP.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()


taskText="notSet"
showBlue = 1
jText = "j=blue"
baseOri = 0
gratingOriA = baseOri-90
gratingOriB = gratingOriA-60
gratingOri  = gratingOriA
thisTrialValue   = "A"


if random() > .5:
    task = "AB"
else:
    task = "A_notA"
lineRed = visual.Line(win=win, name='lineRed',
    start=(-[4][0]/2.0, 0), end=(+[4][0]/2.0, 0),
    ori=1.0, pos=[0, 0],
    lineWidth=20, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
lineBlue = visual.Line(win=win, name='lineBlue',
    start=(-[4][0]/2.0, 0), end=(+[4][0]/2.0, 0),
    ori=1.0, pos=[0, 0],
    lineWidth=20, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1.0,depth=-2.0, 
interpolate=True)
fRed = visual.TextStim(win=win, ori=0, name='fRed',
    text='f=red',    font='Arial',
    pos=[-2.1,1.5], height=0.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
jBlue = visual.TextStim(win=win, ori=0, name='jBlue',
    text='default text',    font='Arial',
    pos=[2.1,1.5], height=0.5, wrapWidth=2,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
instructionText = visual.TextStim(win=win, ori=0, name='instructionText',
    text='default text',    font=u'Arial',
    pos=[0, 3], height=0.5, wrapWidth=20,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "Predictability_Instructions"
Predictability_InstructionsClock = core.Clock()
predictText = "begin exp"
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.5, wrapWidth=20,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "gaborTrial"
gaborTrialClock = core.Clock()


ISI = 1.5 + 1.5
contrastList =np.linspace(.012,.11,9)
noiseTexture = np.random.rand(512,512)*2.0-1
grating = visual.GratingStim(win=win, name='grating',
    tex='sin', mask='gauss',
    ori=1.0, pos=[0, 0], size=[3.8, 3.8], sf=1.6, phase=0.0,
    color=1.0, colorSpace='rgb', opacity=1,
    texRes=256, interpolate=True, depth=-2.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[10, 10],
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
predictabilityBlocks = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='/Users/ales/psychoPyProjects/pikiou/AP.psyexp',
    trialList=data.importConditions('trialPredictabilityList.xlsx'),
    seed=None, name='predictabilityBlocks')
thisExp.addLoop(predictabilityBlocks)  # add the loop to the experiment
thisPredictabilityBlock = predictabilityBlocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPredictabilityBlock.rgb)
if thisPredictabilityBlock != None:
    for paramName in thisPredictabilityBlock.keys():
        exec(paramName + '= thisPredictabilityBlock.' + paramName)

for thisPredictabilityBlock in predictabilityBlocks:
    currentLoop = predictabilityBlocks
    # abbreviate parameter names if possible (e.g. rgb = thisPredictabilityBlock.rgb)
    if thisPredictabilityBlock != None:
        for paramName in thisPredictabilityBlock.keys():
            exec(paramName + '= thisPredictabilityBlock.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    taskBlocks = data.TrialHandler(nReps=10, method='random', 
        extraInfo=expInfo, originPath='/Users/ales/psychoPyProjects/pikiou/AP.psyexp',
        trialList=[None],
        seed=None, name='taskBlocks')
    thisExp.addLoop(taskBlocks)  # add the loop to the experiment
    thisTaskBlock = taskBlocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTaskBlock.rgb)
    if thisTaskBlock != None:
        for paramName in thisTaskBlock.keys():
            exec(paramName + '= thisTaskBlock.' + paramName)
    
    for thisTaskBlock in taskBlocks:
        currentLoop = taskBlocks
        # abbreviate parameter names if possible (e.g. rgb = thisTaskBlock.rgb)
        if thisTaskBlock != None:
            for paramName in thisTaskBlock.keys():
                exec(paramName + '= thisTaskBlock.' + paramName)
        
        #------Prepare to start Routine "Instructions"-------
        t = 0
        InstructionsClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        if task == "AB":
            task = "A_notA"
        else:
            task = "AB"
        
        baseOri = random()*360
        gratingOriA = baseOri-90
        gratingOriB = gratingOriA-60
        
        if random()>.5:
            gratingOri  = gratingOriA
            thisTrialValue   = "A"
        else:
            gratingOri  = gratingOriB
            thisTrialValue   = "B"
        
        if task=="AB":
            taskText = "Press the ""f"" key if the pattern matches the red line\nPress the ""j"" key if the pattern matches the blue line"
            showBlue = 1
            jText = "j=blue"
        elif task=="A_notA":
            taskText = "Press the ""f"" key is the pattern matches the red line\n Otherwise press the ""j"" "
            showBlue = 0
            jText = ""
        
        lineRed.setOri(baseOri)
        lineBlue.setOpacity(showBlue)
        lineBlue.setOri(baseOri - 60)
        jBlue.setText(jText)
        key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_4.status = NOT_STARTED
        instructionText.setText(taskText)
        # keep track of which components have finished
        InstructionsComponents = []
        InstructionsComponents.append(lineRed)
        InstructionsComponents.append(lineBlue)
        InstructionsComponents.append(fRed)
        InstructionsComponents.append(jBlue)
        InstructionsComponents.append(key_resp_4)
        InstructionsComponents.append(instructionText)
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Instructions"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = InstructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *lineRed* updates
            if t >= 0.0 and lineRed.status == NOT_STARTED:
                # keep track of start time/frame for later
                lineRed.tStart = t  # underestimates by a little under one frame
                lineRed.frameNStart = frameN  # exact frame index
                lineRed.setAutoDraw(True)
            
            # *lineBlue* updates
            if t >= 0.0 and lineBlue.status == NOT_STARTED:
                # keep track of start time/frame for later
                lineBlue.tStart = t  # underestimates by a little under one frame
                lineBlue.frameNStart = frameN  # exact frame index
                lineBlue.setAutoDraw(True)
            
            # *fRed* updates
            if t >= 0.0 and fRed.status == NOT_STARTED:
                # keep track of start time/frame for later
                fRed.tStart = t  # underestimates by a little under one frame
                fRed.frameNStart = frameN  # exact frame index
                fRed.setAutoDraw(True)
            
            # *jBlue* updates
            if t >= 0.0 and jBlue.status == NOT_STARTED:
                # keep track of start time/frame for later
                jBlue.tStart = t  # underestimates by a little under one frame
                jBlue.frameNStart = frameN  # exact frame index
                jBlue.setAutoDraw(True)
            
            # *key_resp_4* updates
            if t >= 0.0 and key_resp_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_4.tStart = t  # underestimates by a little under one frame
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_resp_4.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # *instructionText* updates
            if t >= 0.0 and instructionText.status == NOT_STARTED:
                # keep track of start time/frame for later
                instructionText.tStart = t  # underestimates by a little under one frame
                instructionText.frameNStart = frameN  # exact frame index
                instructionText.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InstructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Instructions"-------
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        #------Prepare to start Routine "Predictability_Instructions"-------
        t = 0
        Predictability_InstructionsClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        if trialPredictability==0.5:
            predictText = "For this block target is completely random"
        elif trialPredictability<0.5:
            predictText = "For this block target will usually stay the same"
        elif trialPredictability>0.5:
            predictText = "For this block target will usually alternate"
        
        text_5.setText(predictText)
        key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_5.status = NOT_STARTED
        # keep track of which components have finished
        Predictability_InstructionsComponents = []
        Predictability_InstructionsComponents.append(text_5)
        Predictability_InstructionsComponents.append(key_resp_5)
        for thisComponent in Predictability_InstructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Predictability_Instructions"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = Predictability_InstructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_5* updates
            if t >= 0.0 and text_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_5.tStart = t  # underestimates by a little under one frame
                text_5.frameNStart = frameN  # exact frame index
                text_5.setAutoDraw(True)
            
            # *key_resp_5* updates
            if t >= 0.0 and key_resp_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_5.tStart = t  # underestimates by a little under one frame
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_resp_5.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Predictability_InstructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Predictability_Instructions"-------
        for thisComponent in Predictability_InstructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "Predictability_Instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        targetRandomization = data.TrialHandler(nReps=4, method='random', 
            extraInfo=expInfo, originPath='/Users/ales/psychoPyProjects/pikiou/AP.psyexp',
            trialList=[None],
            seed=None, name='targetRandomization')
        thisExp.addLoop(targetRandomization)  # add the loop to the experiment
        thisTargetRandomization = targetRandomization.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisTargetRandomization.rgb)
        if thisTargetRandomization != None:
            for paramName in thisTargetRandomization.keys():
                exec(paramName + '= thisTargetRandomization.' + paramName)
        
        for thisTargetRandomization in targetRandomization:
            currentLoop = targetRandomization
            # abbreviate parameter names if possible (e.g. rgb = thisTargetRandomization.rgb)
            if thisTargetRandomization != None:
                for paramName in thisTargetRandomization.keys():
                    exec(paramName + '= thisTargetRandomization.' + paramName)
            
            #------Prepare to start Routine "gaborTrial"-------
            t = 0
            gaborTrialClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            noiseTexture = np.random.rand(512,512)*2.0-1
            gC = np.random.choice(contrastList)
            gratingColor = [gC, gC, gC]
            
            if random()<trialPredictability:
            
                if thisTrialValue == "A":
                    gratingOri = gratingOriB
                    thisTrialValue = "B"
                elif thisTrialValue == "B":
                    gratingOri = gratingOriA
                    thisTrialValue = "A"
            
            ISI = random() + 1 + 1.5
            
            thisExp.addData('gratingOri', gratingOri)
            thisExp.addData('thisTrialValue', thisTrialValue)
            thisExp.addData('task',task)
            
            gabor_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
            gabor_response.status = NOT_STARTED
            grating.setColor(gratingColor, colorSpace='rgb')
            grating.setOri(gratingOri)
            image.setImage(noiseTexture)
            # keep track of which components have finished
            gaborTrialComponents = []
            gaborTrialComponents.append(gabor_response)
            gaborTrialComponents.append(grating)
            gaborTrialComponents.append(image)
            for thisComponent in gaborTrialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "gaborTrial"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = gaborTrialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *gabor_response* updates
                if t >= 0.0 and gabor_response.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    gabor_response.tStart = t  # underestimates by a little under one frame
                    gabor_response.frameNStart = frameN  # exact frame index
                    gabor_response.status = STARTED
                    # keyboard checking is just starting
                    gabor_response.clock.reset()  # now t=0
                    event.clearEvents(eventType='keyboard')
                if gabor_response.status == STARTED and t >= (0.0 + (ISI-win.monitorFramePeriod*0.75)): #most of one frame period left
                    gabor_response.status = STOPPED
                if gabor_response.status == STARTED:
                    theseKeys = event.getKeys(keyList=['f', 'j', 'y', 'n', 'left', 'right', 'space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        gabor_response.keys = theseKeys[-1]  # just the last key pressed
                        gabor_response.rt = gabor_response.clock.getTime()
                
                # *grating* updates
                if t >= 0 and grating.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    grating.tStart = t  # underestimates by a little under one frame
                    grating.frameNStart = frameN  # exact frame index
                    grating.setAutoDraw(True)
                if grating.status == STARTED and t >= (0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                    grating.setAutoDraw(False)
                
                # *image* updates
                if t >= 0.0 and image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image.tStart = t  # underestimates by a little under one frame
                    image.frameNStart = frameN  # exact frame index
                    image.setAutoDraw(True)
                if image.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                    image.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in gaborTrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "gaborTrial"-------
            for thisComponent in gaborTrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # check responses
            if gabor_response.keys in ['', [], None]:  # No response was made
               gabor_response.keys=None
            # store data for targetRandomization (TrialHandler)
            targetRandomization.addData('gabor_response.keys',gabor_response.keys)
            if gabor_response.keys != None:  # we had a response
                targetRandomization.addData('gabor_response.rt', gabor_response.rt)
            # the Routine "gaborTrial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 4 repeats of 'targetRandomization'
        
        # get names of stimulus parameters
        if targetRandomization.trialList in ([], [None], None):  params = []
        else:  params = targetRandomization.trialList[0].keys()
        # save data for this loop
        targetRandomization.saveAsExcel(filename + '.xlsx', sheetName='targetRandomization',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
    # completed 10 repeats of 'taskBlocks'
    
# completed 1 repeats of 'predictabilityBlocks'




win.close()
core.quit()