..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   single: adapter pattern
   pair: design patterns; adapter pattern
   single: container adaptors

The Adapter pattern
===================
An adapter converts one interface into another interface that clients expect.
It lets existing code work with a client without changing either the client
or the adapted component.

For example, imagine an existing temperature sensor that reports Celsius:

.. code-block:: cpp
   :name: celsius-sensor-class

   class celsius_sensor{
   public:
     constexpr explicit celsius_sensor(double value)
       :value_{value}
     {}

     constexpr double read_celsius() const {
       return value_;
     }

   private:
     double value_;
   };

Suppose a client expects a sensor with a ``read_fahrenheit()`` operation
instead.  The existing sensor and the client have compatible responsibilities,
but incompatible interfaces.  An adapter supplies the missing conversion:

.. mermaid::
   :alt: Client uses a temperature adapter that forwards to a Celsius sensor
   :align: center

   classDiagram
      Client --> FahrenheitAdapter : uses
      FahrenheitAdapter --> CelsiusSensor : reads
      class FahrenheitAdapter {
         +read_fahrenheit() double
      }
      class CelsiusSensor {
         +read_celsius() double
      }

Traditional adapter implementations
------------------------------------
The traditional design-pattern descriptions distinguish class adapters from
object adapters.

A **class adapter** uses inheritance.  The adapter derives from the adapted
class and adds the interface that clients expect:

.. code-block:: cpp

   class fahrenheit_class_adapter : private celsius_sensor{
   public:
     using celsius_sensor::celsius_sensor;

     constexpr double read_fahrenheit() const {
       return read_celsius() * 9.0 / 5.0 + 32.0;
     }
   };

This approach is simple, but it couples the adapter to one concrete base
class.  The private inheritance keeps ``read_celsius()`` out of the adapter's
public interface.  Clients see the Fahrenheit operation, while the adapter
can still call the inherited Celsius operation internally.

An **object adapter** uses composition.  The adapter stores a reference or
object of the adapted type and delegates through that member:

.. code-block:: cpp

   class fahrenheit_object_adapter{
   public:
     constexpr explicit fahrenheit_object_adapter(
         const celsius_sensor& sensor)
       :sensor_{sensor}
     {}

     constexpr double read_fahrenheit() const {
       return sensor_.read_celsius() * 9.0 / 5.0 + 32.0;
     }

   private:
     const celsius_sensor& sensor_;
   };

Composition avoids an inheritance relationship and lets one adapter wrap an
existing object.  The reference also makes the ownership rule explicit: the
sensor must outlive the adapter.

C++ adapter implementations
---------------------------
C++ does not require a class to inherit from an interface.  A client can use
any object that supplies the operations it needs.  Templates make this
flexibility useful: an adapter can be parameterized by the adapted type
instead of being tied to one concrete class.

Since C++20, a concept can document and check the interface required by the
adapter:

.. code-block:: cpp
   :name: sensor-concept

   template <class Sensor>
   concept celsius_readable = requires(const Sensor& sensor){
     { sensor.read_celsius() } -> std::convertible_to<double>;
   };

The concept does not create a base class or add run-time overhead.  It states
the expressions that a type must support.  The adapter can then use any
matching sensor type:

.. code-block:: cpp
   :name: fahrenheit-adapter

   template <celsius_readable Sensor>
   class fahrenheit_adapter{
   public:
     constexpr explicit fahrenheit_adapter(const Sensor& sensor)
       :sensor_{sensor}
     {}

     constexpr double read_fahrenheit() const {
       return sensor_.read_celsius() * 9.0 / 5.0 + 32.0;
     }

   private:
     const Sensor& sensor_;
   };

This adapter is still an object adapter because it uses composition, but its
interface is checked at compile time and it can wrap any suitable sensor.
There is no virtual function, base class, or run-time type check.

The complete example is small enough to compile and run:

.. tb-code:: cpp
   :include:
      SENSOR: celsius-sensor-class
      CONCEPT: sensor-concept
      ADAPTER: fahrenheit-adapter

   #include <concepts>
   #include <iostream>

   {{SENSOR}}

   {{CONCEPT}}

   {{ADAPTER}}

   int main(){
     celsius_sensor sensor{20.0};
     fahrenheit_adapter adapter{sensor};
     std::cout << "20C == 68F: " << std::boolalpha
               <<  (adapter.read_fahrenheit() == 68.0);
   }

The standard library also uses the adapter pattern for its container
adaptors.  ``std::stack``, ``std::queue``, and ``std::priority_queue`` expose
purpose-specific interfaces over underlying containers.  The next pages use
``std::stack`` and ``std::queue`` as concrete container-adaptor examples;
``std::priority_queue`` is covered later.

.. admonition:: More to Explore

   - :container:`stack`
   - :container:`queue`
   - :container:`priority_queue`
   - `Refactoring Guru: Adapter <https://refactoring.guru/design-patterns/adapter>`__
