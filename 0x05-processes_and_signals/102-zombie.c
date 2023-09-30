#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Sleeps infinitely
 *
 * Return: always 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie proceses
 *
 * Return: always 0.
 */

int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid < 0)
		{
			perror("Fork failed");
			exit(1);
		}
		else if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		else
		{

		}
	}

	infinite_while();

	return (0);
}
