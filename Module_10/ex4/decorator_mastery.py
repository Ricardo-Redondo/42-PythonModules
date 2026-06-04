import functools
import time
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        print(f"casting {func.__name__}...")
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = kwargs.get("power") or (
                args[2] if len(args) > 2 else args[1] if len(args) > 1 else 0)

            if power >= min_power:
                return func(*args, **kwargs)
            return "insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "fireball cast!"

    print("\033[33mtesting spell timer...\033[0m")
    print(f"result: {fireball()}")

    print("\n\033[33mtesting retrying spell...\033[0m")

    @retry_spell(max_attempts=3)
    def unstable_portal():
        raise ValueError("portal collapsed!")
    print(unstable_portal())
    print("Waaaaaaagh spelled !")

    print("\n\033[33mtesting mageguild...\033[0m")
    guild = MageGuild()

    print("name validation:")
    print(guild.validate_mage_name('gandalf'))
    print(guild.validate_mage_name('12'))

    print()
    print(guild.cast_spell("lightning", 15))
    print(guild.cast_spell("spark", 5))
