# !/usr/bin/env python3
"""
    WHEA Robotics 3881 code for FRC 2020.
"""

#==>> Rod's comments 2020-03-07 preceeded by the wide arrow.
"""
 (Rod is our programming mentor, an increadible resource of knowlage and great person)
"""

import wpilib
import ctre
import wpilib.drive
from rev.color import ColorSensorV3
from rev.color import ColorMatch
import time


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        # Set up drive train motor controllers, Falcon 500 using TalonFX.
        self.l_motorBack = ctre.TalonFX(1)
        self.l_motorBack.setInverted(True)

        self.r_motorBack = ctre.TalonFX(2)

        self.l_motorFront = ctre.TalonFX(3)
        self.l_motorFront.setInverted(True)

        self.r_motorFront = ctre.TalonFX(4)

        self.l_motorBack.follow(self.l_motorFront)
        self.r_motorBack.follow(self.r_motorFront)

        self.l_motorBack.setInverted(ctre._ctre.InvertType.FollowMaster)
        self.r_motorBack.setInverted(ctre._ctre.InvertType.FollowMaster)

        self.l_motorBack.setNeutralMode(ctre._ctre.NeutralMode.Coast)
        self.l_motorFront.setNeutralMode(ctre._ctre.NeutralMode.Coast)
        self.r_motorBack.setNeutralMode(ctre._ctre.NeutralMode.Coast)
        self.r_motorFront.setNeutralMode(ctre._ctre.NeutralMode.Coast)

        # Set up joystick objects.
        self.l_joy = wpilib.Joystick(0)
        self.r_joy = wpilib.Joystick(1)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""

        #This resets and calls variables when the autonomous period begins
        self.l_motorFront.setSelectedSensorPosition(0)
        self.r_motorFront.setSelectedSensorPosition(0)

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        
        # Get joystick values once (so that we are guaranteed to send each motor the same value).
        left_command = self.l_joy.getRawAxis(1)
        right_command = self.r_joy.getRawAxis(1)

        # self.l_motorFront.set(ctre._ctre.ControlMode.PercentOutput, left_command)
        self.l_motorFront.set(ctre._ctre.ControlMode.PercentOutput, left_command)
        # self.l_motorBack.set(ctre._ctre.ControlMode.PercentOutput, left_command)
        self.r_motorFront.set(ctre._ctre.ControlMode.PercentOutput, right_command)
        # self.r_motorBack.set(ctre._ctre.ControlMode.PercentOutput, right_command)


if __name__ == "__main__":
    wpilib.run(MyRobot)

